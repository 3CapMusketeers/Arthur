(function(t){function e(e){for(var r,a,i=e[0],c=e[1],l=e[2],u=0,d=[];u<i.length;u++)a=i[u],Object.prototype.hasOwnProperty.call(o,a)&&o[a]&&d.push(o[a][0]),o[a]=0;for(r in c)Object.prototype.hasOwnProperty.call(c,r)&&(t[r]=c[r]);p&&p(e);while(d.length)d.shift()();return s.push.apply(s,l||[]),n()}function n(){for(var t,e=0;e<s.length;e++){for(var n=s[e],r=!0,a=1;a<n.length;a++){var i=n[a];0!==o[i]&&(r=!1)}r&&(s.splice(e--,1),t=c(c.s=n[0]))}return t}var r={},a={app:0},o={app:0},s=[];function i(t){return c.p+"js/"+({about:"about"}[t]||t)+"."+{about:"2074c6b2"}[t]+".js"}function c(e){if(r[e])return r[e].exports;var n=r[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,c),n.l=!0,n.exports}c.e=function(t){var e=[],n={about:1};a[t]?e.push(a[t]):0!==a[t]&&n[t]&&e.push(a[t]=new Promise((function(e,n){for(var r="css/"+({about:"about"}[t]||t)+"."+{about:"95efa3f3"}[t]+".css",o=c.p+r,s=document.getElementsByTagName("link"),i=0;i<s.length;i++){var l=s[i],u=l.getAttribute("data-href")||l.getAttribute("href");if("stylesheet"===l.rel&&(u===r||u===o))return e()}var d=document.getElementsByTagName("style");for(i=0;i<d.length;i++){l=d[i],u=l.getAttribute("data-href");if(u===r||u===o)return e()}var p=document.createElement("link");p.rel="stylesheet",p.type="text/css",p.onload=e,p.onerror=function(e){var r=e&&e.target&&e.target.src||o,s=new Error("Loading CSS chunk "+t+" failed.\n("+r+")");s.code="CSS_CHUNK_LOAD_FAILED",s.request=r,delete a[t],p.parentNode.removeChild(p),n(s)},p.href=o;var f=document.getElementsByTagName("head")[0];f.appendChild(p)})).then((function(){a[t]=0})));var r=o[t];if(0!==r)if(r)e.push(r[2]);else{var s=new Promise((function(e,n){r=o[t]=[e,n]}));e.push(r[2]=s);var l,u=document.createElement("script");u.charset="utf-8",u.timeout=120,c.nc&&u.setAttribute("nonce",c.nc),u.src=i(t);var d=new Error;l=function(e){u.onerror=u.onload=null,clearTimeout(p);var n=o[t];if(0!==n){if(n){var r=e&&("load"===e.type?"missing":e.type),a=e&&e.target&&e.target.src;d.message="Loading chunk "+t+" failed.\n("+r+": "+a+")",d.name="ChunkLoadError",d.type=r,d.request=a,n[1](d)}o[t]=void 0}};var p=setTimeout((function(){l({type:"timeout",target:u})}),12e4);u.onerror=u.onload=l,document.head.appendChild(u)}return Promise.all(e)},c.m=t,c.c=r,c.d=function(t,e,n){c.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},c.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},c.t=function(t,e){if(1&e&&(t=c(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(c.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var r in t)c.d(n,r,function(e){return t[e]}.bind(null,r));return n},c.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return c.d(e,"a",e),e},c.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},c.p="/",c.oe=function(t){throw console.error(t),t};var l=window["webpackJsonp"]=window["webpackJsonp"]||[],u=l.push.bind(l);l.push=e,l=l.slice();for(var d=0;d<l.length;d++)e(l[d]);var p=u;s.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("cd49")},"0c49":function(t,e,n){"use strict";var r=n("6dcb"),a=n.n(r);a.a},"3b3d":function(t,e,n){},"4c2a":function(t,e,n){"use strict";var r=n("3b3d"),a=n.n(r);a.a},"6dcb":function(t,e,n){},"73ec":function(t,e,n){},cd49:function(t,e,n){"use strict";n.r(e);var r=n("2b0e"),a=n("2f62");r["default"].use(a["a"]);var o=new a["a"].Store({state:{},mutations:{},actions:{},modules:{}}),s=n("8c4f"),i=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"home"},[n("div",[n("video-page")],1)])},c=[],l=n("9ab4"),u=n("60a3");let d=class extends u["b"]{constructor(){super(...arguments),this.options={normalScrollElements:".video-sidebar",dragAndMove:"fingersonly"}}};d=Object(l["a"])([Object(u["a"])({components:{}})],d);var p=d,f=p,b=(n("0c49"),n("2877")),m=Object(b["a"])(f,i,c,!1,null,"aa0bd3c6",null),h=m.exports,v=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},g=[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"login"},[n("div",{staticClass:"row justify-content-center h-100"},[n("form",{staticClass:"form-signin col-3 align-middle"},[n("img",{staticClass:"mb-4",attrs:{src:"https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg",alt:"",width:"72",height:"72"}}),n("h1",{staticClass:"h3 mb-3 font-weight-normal"},[t._v("Please sign in")]),n("label",{staticClass:"sr-only",attrs:{for:"inputEmail"}},[t._v("Email address")]),n("input",{staticClass:"form-control",attrs:{type:"email",id:"inputEmail",placeholder:"Email address",required:"",autofocus:"","data-keeper-lock-id":"k-j0h2m7ayf0f"}}),n("label",{staticClass:"sr-only",attrs:{for:"inputPassword"}},[t._v("Password")]),n("input",{staticClass:"form-control",attrs:{type:"password",id:"inputPassword",placeholder:"Password",required:"","data-keeper-lock-id":"k-p0z2lkb807"}}),n("div",{staticClass:"checkbox mb-3"},[n("label",[n("input",{attrs:{type:"checkbox",value:"remember-me"}}),t._v(" Remember me ")])]),n("button",{staticClass:"btn btn-lg btn-primary btn-block",attrs:{type:"submit"}},[t._v("Sign in")]),n("p",{staticClass:"mt-5 mb-3 text-muted"},[t._v("© 2017-2018")])])])])}];let y=class extends u["b"]{};y=Object(l["a"])([Object(u["a"])({components:{}})],y);var w=y,_=w,j=(n("d6db"),Object(b["a"])(_,v,g,!1,null,null,null)),O=j.exports;r["default"].use(s["a"]);const C=[{path:"/",name:"Home",component:h},{path:"/login",name:"Login",component:O},{path:"/dashboard",name:"Dashboard",component:()=>n.e("about").then(n.bind(null,"7277"))},{path:"/about",name:"About",component:()=>n.e("about").then(n.bind(null,"f820"))}],k=new s["a"]({routes:C});var E=k,x=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"}},[t._v(" Lancelot ")])},P=[];let S=class extends u["b"]{};S=Object(l["a"])([Object(u["a"])({components:{}})],S);var A=S,L=A,T=(n("4c2a"),Object(b["a"])(L,x,P,!1,null,"59a8fd59",null)),M=T.exports,N=n("5f5b"),$=n("b1e0");n("73ec");r["default"].use(N["a"]),r["default"].use($["a"]),new r["default"]({store:o,router:E,render:t=>t(M)}).$mount("#app")},d6db:function(t,e,n){"use strict";var r=n("e67a"),a=n.n(r);a.a},e67a:function(t,e,n){}});
//# sourceMappingURL=app.0b892c00.js.map