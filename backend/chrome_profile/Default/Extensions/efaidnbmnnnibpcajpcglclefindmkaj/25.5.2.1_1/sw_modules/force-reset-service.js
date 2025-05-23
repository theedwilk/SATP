/*************************************************************************
* ADOBE CONFIDENTIAL
* ___________________
*
*  Copyright 2015 Adobe Systems Incorporated
*  All Rights Reserved.
*
* NOTICE:  All information contained herein is, and remains
* the property of Adobe Systems Incorporated and its suppliers,
* if any.  The intellectual and technical concepts contained
* herein are proprietary to Adobe Systems Incorporated and its
* suppliers and are protected by all applicable intellectual property laws,
* including trade secret and or copyright laws.
* Dissemination of this information or reproduction of this material
* is strictly forbidden unless prior written permission is obtained
* from Adobe Systems Incorporated.
**************************************************************************/
import{dcLocalStorage as e}from"../common/local-storage.js";import{common as t}from"./common.js";import{Proxy as a}from"./proxy.js";const r="floodgate-rollback";class s{#e;#t;#a;#r;constructor(){this.#e=a.proxy.bind(this),this.#t={data:{},timestamp:0},this.#a=null,this.#r=new Map}async#s(){try{const e=t.getOteConfigUrl(),a=await fetch(e);if(!a.ok)throw new Error(`HTTP error! status: ${a.status}`);return await a.json()}catch(e){return console.error("Error fetching one-time executor config:",e),{}}}#o(e){return this.#t.data&&e-this.#t.timestamp<3e4}#i(e,t){this.#t.data=e,this.#t.timestamp=t}async fetchOneTimeExecutorConfig(){const e=Date.now();return this.#o(e)?this.#t.data:(this.#a||(this.#a=(async()=>{try{const t=new Promise((e=>setTimeout((()=>e(null)),5e3))),a=await Promise.race([t,this.#s()]);return this.#i(a,e),a}finally{this.#a=null}})()),this.#a)}#c(e){return Array.isArray(e.rollbackFeatureFlags)}#n(t){t.length>0?e.setItem(r,t.join(",")):e.removeItem(r)}async getFeatureConfig(e){const t=await this.fetchOneTimeExecutorConfig();return t?(this.#c(t)&&this.#n(t.rollbackFeatureFlags),t.oneTimeActivities?.[e]??{}):{}}#l(e){return!(!e||0===Object.keys(e).length)&&!!e.id}#u(e,t){return!(!e||"function"!=typeof t)||(console.error("Invalid parameters: featureName and executeCallback are required"),!1)}async#h(e){let t;new Promise((a=>{t=a,this.#r.set(e,t)}));return t}#f(e,t){t&&(t(),this.#r.delete(e))}#g(e,a){const r=t.isAdobeInternalUser();return e&&r||a&&!r}async#m(a,r){try{const s=await this.getFeatureConfig(a);if(!this.#l(s))return{};const{id:o,adobeInternal:i=!1,adobeExternal:c=!1}=s,n=`ote-${a}-${t.getEnv()}`;return e.getItem(n)===o||(this.#g(i,c)?(e.setItem(n,o),await r(s)):console.log(`Feature ${a} is not applicable for the current user.`)),s}catch(e){return console.error(`Error executing feature ${a}:`,e),{}}}async executeFeature(e,t){if(!this.#u(e,t))return{};if(this.#r.has(e))return{};const a=await this.#h(e);try{return await this.#m(e,t)}finally{this.#f(e,a)}}async getRollbackFeatureFlags(){const e=await this.fetchOneTimeExecutorConfig();e&&this.#c(e)&&this.#n(e.rollbackFeatureFlags)}async getFloodgateTTLs(){const t=await this.fetchOneTimeExecutorConfig();if(t&&t.floodgateTTLs&&Object.keys(t.floodgateTTLs).length>0)for(const[a,r]of Object.entries(t.floodgateTTLs))e.setItem(a,r)}}export const forceResetService=new s;export const TestForceResetService=s;