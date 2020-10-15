<template>
  <div class="login">
    <div class="row h-100 d-flex justify-content-center align-items-center">
      <form class="form-signin col-3 align-middle">
        <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
        <b-button variant="primary" :href="url">Login with Spotify</b-button>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from "vue-property-decorator";
import SpotifyDataService from "@/services/SpotifyDataService";
import router from "@/router";

@Component({
  components: {}
})
export default class Login extends Vue {
  url: string;

  mounted() {
    const url = this.$route.hash.slice(1);
    const parsed = this.parse_query_string(url);
    if (parsed.has('access_token')) {
      SpotifyDataService.login(parsed.get("access_token"));
      SpotifyDataService.setUsername(parsed.get("access_token"));
      router.push('/');
    }
}
  constructor() {
    super();
    var path = this.$router.resolve({name: 'Login'}).href
    var fullUrl = window.location.origin + path;
    this.url = SpotifyDataService.getSpotifyURL(encodeURI(fullUrl));
  }

  parse_query_string(query: string) {
    let vars = query.split("&");
    let query_string = new Map();

    for (var i = 0; i < vars.length; i++) {
      var pair = vars[i].split("=");
      var key = decodeURIComponent(pair[0]);
      var value = decodeURIComponent(pair[1]);

      const arr = decodeURIComponent(value);

      query_string.set(key, arr);

    }
    return query_string;
  }


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

