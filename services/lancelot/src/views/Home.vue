<template>
  <div class="home">
    <div class="row h-100 d-flex justify-content-center align-items-center">
      <div class="col">
        <h2 class="text-center">
          Camelot
        </h2>
        <div class="row google-form text-center d-flex justify-content-center">
          <form action="http://google.com/search" method="get" class="col-8">
            <div class="form-group">
              <input type="text" class="form-control google-search" name="q">
              <div class="btn-group ">
                <b-button variant="primary" @click="createPlaylist()">Create Playlist</b-button>
                <b-button variant="primary" @click="getDiscover()">Discover</b-button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {Component, Vue} from "vue-property-decorator";

@Component({
  components: {}
})
export default class Home extends Vue {

  createPlaylist() {
    console.log('click Createplaylist')
  }

  getDiscover() {
    console.log('clicked get discover')
  }


  // private tutorial: any = {
  //   id: null,
  //   title: "",
  //   description: "",
  //   published: false,
  // };
  //
  // private submitted: boolean = false;
  //
  // saveTutorial() {
  //   var data = {
  //     title: this.tutorial.title,
  //     description: this.tutorial.description,
  //   };
  //
  //   TutorialDataService.create(data)
  //     .then((response) => {
  //       this.tutorial.id = response.data.id;
  //       console.log(response.data);
  //       this.submitted = true;
  //     })
  //     .catch((e) => {
  //       console.log(e);
  //     });
  // }
  //
  // newTutorial() {
  //   this.submitted = false;
  //   this.tutorial = {};
  // }
}
</script>

<style scoped lang="scss">
.home {
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
