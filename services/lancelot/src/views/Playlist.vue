<template>
  <div class="playlist">
    <div class="row h-100 d-flex justify-content-center">
      <div class="col">
        <div class="row text-center">
          <div class="input-group">
            <input type="text" class="form-control google-search" name="q">
            <b-button variant="primary ml-3">Create Playlist</b-button>
            <b-button variant="primary mx-3">Discover</b-button>
          </div>
        </div>

        <table class="table">
          <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Song</th>
            <th scope="col">Artist</th>
            <th scope="col">Include</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="track in tracks" v-bind:key="track.id">
            <th scope="row">{{track.id}}</th>
            <td>{{track.song}}</td>
            <td>{{track.artist}}</td>
            <td>
              <input type="checkbox" aria-label="Checkbox for following text input">
            </td>
          </tr>
          </tbody>
        </table>
        <div class="d-flex justify-content-center">
          <b-button variant="primary">
            <b-icon icon="plus"></b-icon>
            Save Playlist
          </b-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from "vue-property-decorator";

@Component({
  components: {},
})
export default class Playlist extends Vue {
  tracks = {};
 mounted() {
  this.tracks = this.$store.getters.tracks;
 }
}
</script>

<style scoped lang="scss">
.playlist {
  height: 60vh;
}

.google-logo {
  padding: 20px 0;
}

.google-search {
  padding: 20px 10px;
}

.google-search:focus {
  box-shadow: silver 0 2px 10px;
  border-color: silver;
}

.google-form .btn-group {
  padding: 20px 0;
}

.btn-group > .btn {
  border-radius: 0;
  margin: 0 10px;
}


</style>
