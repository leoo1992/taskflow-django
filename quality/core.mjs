/** @param {number} passed @param {number} total */
export function qualityPercent(passed,total){if(!Number.isFinite(passed)||!Number.isFinite(total)||total<=0)return 0;return Math.round(passed/total*100)}
/** @param {string} path */
export function isSensitivePath(path){const n=path.toLowerCase();if(/(^|\/)\.env(?:\.|$)/.test(n)&&!(/\.(example|sample|template)$/.test(n)))return true;return /\.(pem|key|p12|pfx|jks|keystore)$/.test(n)}
