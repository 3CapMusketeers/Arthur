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

  login(token: string) {
    let actualToken = localStorage.setItem('spotify_token', token);
    return actualToken;
  }

  createPlaylist(term: string) {
    return http.post(`/users/${this.getToken()}/saved-tracks?search_term=${term}`, {})
  }

  isLoggedIn() {
    return (this.getToken() != null && this.getUsername() != null)
  }

  getUsername():string {
    return <string>localStorage.getItem('username');
  }

  getToken() {
    return localStorage.getItem('spotify_token');
  }

  setUsername(token: string): boolean {
    const fd = new FormData();
    let res = false;
    fd.append('access_token', token)
    http.post(`/`, fd).then(data => {
      if('error' in data.data && data.data.error) {
        res = false;
      } else {
        localStorage.setItem('username', data.data.user);
        res = true;
      }
    });
    return res;
    // return false;
  }

  logout() {
    localStorage.removeItem('username');
    localStorage.removeItem('spotify_token');
  }

}

export default new SpotifyDataService()
