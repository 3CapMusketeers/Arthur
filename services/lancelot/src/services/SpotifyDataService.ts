import http from "../http-common";
import router from "@/router";

class SpotifyDataService {
  clientId = "369a6c4b828e4dda98c6a47e891d5b2f";
  scopes = ["user-read-private", "user-library-read"];
  // redirectUri = "http://localhost:8080/login"; //Use route for this to get current url
  authEndpoint = "https://accounts.spotify.com/authorize";

  getSpotifyURL(spotifyCallback: string) {
    return (
      this.authEndpoint +
      "?client_id=" +
      this.clientId +
      "&redirect_uri=" +
      spotifyCallback +
      "&scope=" +
      this.scopes.join("%20") +
      "&response_type=token&show_dialog=true"
    );
  }

  // login(token: string) {
  //   let actualToken = localStorage.setItem('spotify_token', token);
  //   return actualToken;
  // }

  savePlaylist(name: string, tracks: any, token: string) {
    const fd = new FormData();
    fd.append("access_token", token);
    fd.append("name", name);

    let trackids: string[] = [];

    tracks.forEach((track: { uri: string; }) => {
      trackids.push(track.uri);
    });
    console.log('tracks: ', trackids);
    console.log('name: ', name);

    //@ts-ignore
    fd.append("uris", trackids);
    return http.post(`/users/playlists`, fd);
  }

  createPlaylist(term: string, token: string) {
    const fd = new FormData();
    fd.append("access_token", token);

    return http.post(`/users/saved-tracks?search_term=${term}`, fd);
  }

  discover(term: string, token: string) {
    const fd = new FormData();
    fd.append("access_token", token);
    return http.post(`/users/recommended?search_term=${term}`, fd);
  }

  checkModelCreated(token: string) {
    const fd = new FormData();
    fd.append("access_token", token);
    return http.post(`/`, fd);
  }
  async getUsername(token: string) {
    const fd = new FormData();
    fd.append("access_token", token);

    try {
      const response = await http.post(`/`, fd);
      console.log(response.data.user);
      return response.data.user;
    } catch (error) {
      // @ts-ignore
      this.$store.commit('logout');
      console.log(error);
      return "";
    }
  }

  // logout() {
  //   localStorage.removeItem('username');
  //   localStorage.removeItem('spotify_token');
  // }
}

export default new SpotifyDataService();
