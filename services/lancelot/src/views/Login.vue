<template>
  <div class="login">
    <div class="row h-100 d-flex justify-content-center align-items-center">
      <form class="form-signin col-3 align-middle">
        <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
        Spotify Login Button
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from "vue-property-decorator";

@Component({
  components: {}
})
export default class Login extends Vue {
}
</script>
<style>
.login {
  height: 60vh;
}

.
.form-signin {
  padding: 20px;
  border: 1px solid #2c3e50;
  border-radius: 20px;
}
</style>

