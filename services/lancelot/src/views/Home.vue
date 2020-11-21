<template>
  <div class="home">
    <div class="row h-100 d-flex justify-content-center align-items-center">
      <div class="col">
        <h2 class="text-center">
          Camelot
        </h2>
        <div class="row google-form text-center d-flex justify-content-center">
          <div v-if="loading" class="col">
            <div>
              <b-spinner
                style="width: 4rem; height: 4rem;"
                class="mt-5 mb-4"
                label="Large Spinner"
              ></b-spinner>
            </div>
            <h5>Generating a great playlist!</h5>
            <small class="text-muted">(Get some snacks while you wait)</small>
          </div>
          <div v-else class="form-group col-8">
            <input v-model="searchTerm" class="form-control google-search" />
            <div class="btn-group" v-if="modelExists">
              <b-button variant="primary" @click="createPlaylist()"
                >Create Playlist</b-button
              >
              <b-button variant="primary" @click="getDiscover()"
                >Discover</b-button
              >
            </div>
            <div v-else class="col">
              <h5 class="btn-group text-muted">
                Please wait while we are creating your model
              </h5>
              {{interval}}
              <b-button variant="link" @click="checkModel">Force Refresh</b-button>
              <b-button variant="link" @click="stopTimer">Stop Timer</b-button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import SpotifyDataService from "@/services/SpotifyDataService";

@Component({
  components: {},
  computed: {
    isAuth() {
      return this.$store.getters.authenticated;
    },
    token() {
      return this.$store.getters.userToken;
    }
  }
})
export default class Home extends Vue {
  searchTerm = "";
  loading = false;
  modelExists = false;
  interval = 180;
  sentCreateRequest = false; 

  countDownTimer() {
    if(this.interval> 0) {
      setTimeout(() => {
        this.interval -= 1;
        this.countDownTimer();
      }, 1000);
    } else {
      const model = this.checkModel();
      if(!model) {
        this.interval = 180;
        this.countDownTimer();
      } else {
        this.modelExists = true;
      }
    }
  }

  stopTimer() {
    this.interval = 0;
  }
  mounted() {
    this.countDownTimer();
  }
  checkModel() {
    SpotifyDataService.checkModelCreated(this.token, this.sentCreateRequest).then(d => {
      this.sentCreateRequest = true; 
      if(d.status==204) {
        return false;
      } else {
        this.sentCreateRequest = false; 
        return true;
      }
    });
  }
  createPlaylist() {
    this.loading = true;
    // eslint-disable-next-line
    SpotifyDataService.createPlaylist(this.searchTerm, this.token)
      .then(d => {
        this.$store.commit("changeTracks", d.data.tracks);
        console.log(d);
        this.$router.push({ name: "Playlist" });
      })
      .finally(() => (this.loading = false));
  }

  getDiscover() {
    this.loading = true;
    // eslint-disable-next-line
    SpotifyDataService.createPlaylist(this.searchTerm, this.token)
      .then(d => {
        this.$store.commit("changeTracks", d.data.tracks);
        console.log(d);
        this.$router.push({ name: "Playlist" });
      })
      .finally(() => (this.loading = false));
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
