import http from "../http-common";
import axios from "axios";

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

  storeToken(token: string) {
    return localStorage.setItem('spotify_token', token);
  }

  getToken() {
    return localStorage.getItem('spotify_token');
  }

  get() {
    return http.get(`/?access_token=${this.getToken()}`);
  }


}

export default new SpotifyDataService()
