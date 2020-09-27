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
          <tr>
            <th scope="row">1</th>
            <td>Ultralight Beam</td>
            <td>Kanye West</td>
            <td>
              <input type="checkbox" aria-label="Checkbox for following text input">
            </td>
          </tr>
          <tr>
            <th scope="row">2</th>
            <td>Ultralight Beam</td>
            <td>Kanye West</td>
            <td>
              <input type="checkbox" aria-label="Checkbox for following text input">
            </td>
          </tr>
          <tr>
            <th scope="row">3</th>
            <td>Ultralight Beam</td>
            <td>Kanye West</td>
            <td>
              <input type="checkbox" aria-label="Checkbox for following text input">
            </td>
          </tr>
          <tr>
            <th scope="row">4</th>
            <td>Ultralight Beam</td>
            <td>Kanye West</td>
            <td>
              <input type="checkbox" aria-label="Checkbox for following text input">
            </td>
          </tr>
          <tr>
            <th scope="row">5</th>
            <td>Ultralight Beam</td>
            <td>Kanye West</td>
            <td>
              <input type="checkbox" aria-label="Checkbox for following text input">
            </td>
          </tr>
          <tr>
            <th scope="row">6</th>
            <td>Ultralight Beam</td>
            <td>Kanye West</td>
            <td>
              <input type="checkbox" aria-label="Checkbox for following text input">
            </td>
          </tr>
          <tr>
            <th scope="row">7</th>
            <td>Ultralight Beam</td>
            <td>Kanye West</td>
            <td>
              <input type="checkbox" aria-label="Checkbox for following text input">
            </td>
          </tr>
          <tr>
            <th scope="row">8</th>
            <td>Ultralight Beam</td>
            <td>Kanye West</td>
            <td>
              <input type="checkbox" aria-label="Checkbox for following text input">
            </td>
          </tr>
          <tr>
            <th scope="row">9</th>
            <td>Ultralight Beam</td>
            <td>Kanye West</td>
            <td>
              <input type="checkbox" aria-label="Checkbox for following text input">
            </td>
          </tr>
          <tr>
            <th scope="row">10</th>
            <td>Ultralight Beam</td>
            <td>Kanye West</td>
            <td>
              <input type="checkbox" aria-label="Checkbox for following text input">
            </td>
          </tr>
          <tr>
            <th scope="row">11</th>
            <td>Ultralight Beam</td>
            <td>Kanye West</td>
            <td>
              <input type="checkbox" aria-label="Checkbox for following text input">
            </td>
          </tr>
          <tr>
            <th scope="row">12</th>
            <td>Ultralight Beam</td>
            <td>Kanye West</td>
            <td>
              <input type="checkbox" aria-label="Checkbox for following text input">
            </td>
          </tr>
          <tr>
            <th scope="row">13</th>
            <td>Ultralight Beam</td>
            <td>Kanye West</td>
            <td>
              <input type="checkbox" aria-label="Checkbox for following text input">
            </td>
          </tr>

          </tbody>
        </table>


      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from "vue-property-decorator";

@Component({
  components: {}
})
export default class Playlist extends Vue {
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
