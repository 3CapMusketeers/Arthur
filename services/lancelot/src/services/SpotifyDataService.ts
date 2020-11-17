import http from "../http-common";
import router from "@/router";

class SpotifyDataService {
  clientId = "369a6c4b828e4dda98c6a47e891d5b2f";
  scopes = [
    'user-read-private',
    'user-library-read'
  ];
  // redirectUri = "http://localhost:8080/login"; //Use route for this to get current url
  authEndpoint = 'https://accounts.spotify.com/authorize';

  getSpotifyURL(spotifyCallback: string) {
    return this.authEndpoint + "?client_id=" + this.clientId + "&redirect_uri=" + spotifyCallback + "&scope=" + this.scopes.join('%20') + "&response_type=token&show_dialog=true";
  }

  // login(token: string) {
  //   let actualToken = localStorage.setItem('spotify_token', token);
  //   return actualToken;
  // }

  savePlaylist(name: string, tracks: any) {
    const fd = new FormData();
    fd.append('access_token', this.$store.userToken());
    fd.append('name', name);
    fd.append('uris', tracks)
    return http.post(`/users/playlists`, fd);
  }

  createPlaylist(term: string) {
    const fd = new FormData();
    fd.append('access_token', this.$store.userToken());

    return http.post(`/users/saved-tracks?search_term=${term}`, fd);
  }

  discover(term: string) {
    const fd = new FormData();
    fd.append('access_token', this.$store.userToken());
    return http.post(`/users/recommended?search_term=${term}`, fd);
  }

  // isLoggedIn() {
  //   return (this.getToken() != null && this.getUsername() != null)
  // }

  // getUsername():string {
  //   return <string>localStorage.getItem('username');
  // }

  // getToken(): string {
  //   return <string>localStorage.getItem('spotify_token');
  // }

  getUsername(token: string): string {
    const fd = new FormData();
    let res = "";
    fd.append('access_token', token)
    http.post(`/`, fd).then(data => {
        res = data.data.user;
    });
    return res;
  }

  // logout() {
  //   localStorage.removeItem('username');
  //   localStorage.removeItem('spotify_token');
  // }

}

export default new SpotifyDataService()
