import http from "../http-common";
import router from "@/router";

class SpotifyDataService {
  clientId = "369a6c4b828e4dda98c6a47e891d5b2f";
  scopes = [
    'user-read-private',
    'user-library-read'
  ];
  redirectUri = "http://localhost:8080/login";
  authEndpoint = 'https://accounts.spotify.com/authorize';

  getSpotifyURL() {
    return this.authEndpoint + "?client_id=" + this.clientId + "&redirect_uri=" + this.redirectUri + "&scope=" + this.scopes.join('%20') + "&response_type=token&show_dialog=true";
  }

  login(token: string) {
    let actualToken = localStorage.setItem('spotify_token', token);
    this.setUsername()
    return actualToken;
  }

  getUsername() {
    return <string>localStorage.getItem('username');
  }

  getToken() {
    return localStorage.getItem('spotify_token');
  }

  setUsername() {
    http.get(`/?access_token=${this.getToken()}`).then(data => {
      return localStorage.setItem('username', data.data.user);
    });
  }

  logout() {
    localStorage.removeItem('username');
    localStorage.removeItem('spotify_token');
  }

}

export default new SpotifyDataService()
