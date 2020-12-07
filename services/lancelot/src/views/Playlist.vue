<template>
  <div class="playlist">
    <div class="row h-100 table eh">
      <div class="col">
        <!--        <div class="row text-center">-->
        <!--          <div class="input-group">-->
        <!--            <input type="text" class="form-control google-search" name="q">-->
        <!--            <b-button variant="primary ml-3">Create Playlist</b-button>-->
        <!--            <b-button variant="primary mx-3">Discover</b-button>-->
        <!--          </div>-->
        <!--        </div>-->
        <div class="row p-2">
          <b-input v-model="name" placeholder="Playlist Name"></b-input>
          <b-button variant="primary" @click="savePlaylist()">
            <b-icon icon="plus"></b-icon>
            Save Playlist
          </b-button>
          <b-button size="sm" @click="selectAllRows">Select all</b-button>
          <b-button size="sm" @click="clearSelected">Clear selected</b-button>
        </div>
        <div>Select Songs to save</div>
        <b-table
          class="table"
          ref="selectableTable"
          sticky-header="650px"
          selectable
          :hover="true"
          :striped="true"
          :items="tracks"
          :fields="fields"
          @row-selected="onRowSelected"
        >
          <template #cell(index)="data">
            {{ data.index + 1 }}
          </template>
          <template #cell(selected)="{ rowSelected }">
            <template v-if="rowSelected">
              <span aria-hidden="true">&check;</span>
              <span class="sr-only">Selected</span>
            </template>
            <template v-else>
              <span aria-hidden="true">&nbsp;</span>
              <span class="sr-only">Not selected</span>
            </template>
          </template>
        </b-table>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from "vue-property-decorator";
import SpotifyDataService from "@/services/SpotifyDataService";

@Component({
  components: {},
})
export default class Playlist extends Vue {
  tracks = {};
  index = 0;
  name = "Camelot Playlist";
  fields = ["selected", "index", "name", "artists"];
  selected = [];


  mounted() {
    this.tracks = this.$store.getters.tracks;
    this.$nextTick(function () {
      this.$refs.selectableTable.selectAllRows();
    });
  }


  savePlaylist() {
    SpotifyDataService.savePlaylist(this.name, this.tracks, this.$store.getters.userToken).then(d => {
      console.log(d);
    });
  }

  onRowSelected(items) {
    this.selected = items;
  }

  selectAllRows() {
    this.$refs.selectableTable.selectAllRows();
  }

  clearSelected() {
    this.$refs.selectableTable.clearSelected();
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
