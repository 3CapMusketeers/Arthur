<template>
  <div id="app">
    Lancelot
  </div>
</template>
<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({
  components: {}
})
export default class Login extends Vue {}
</script>
<style scoped type="scss">
#sticky-sidebar {
  position: fixed;
  right: 0px;
  left: 0px;
}

.sidebarMenu {
}

html {
  height: 100%;
}

body {
  min-height: 100vh;
}

/* fixed and fluid only on sm and up */
@media (min-width: 768px) {
  .left {
    position: fixed;
  }
  .fixed {
    min-height: 100vh;
    min-width: 260px;
    max-width: 260px;
  }
  .col .fluid {
    min-height: 100vh;
  }
  .flex-grow {
    flex: 1;
  }
  #topNav {
    width: calc(100vh-200px);
    margin-left: 260px;
  }
}
</style>

