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
    // this.setUsername()

    return actualToken;
  }

  getRecommendation(term: string) {
    http.post(`/users/${this.getToken()}/recommended?search_term=${term}`, {}).then(d => {
      if(d.data.length==0) {
        //empty
        console.log(d.data)
      }
      console.log(d.data)
    });
  }

  getUsername() {
    return <string>localStorage.getItem('username');
  }

  getToken() {
    return localStorage.getItem('spotify_token');
  }

  setUsername(token: string) {
    const fd = new FormData();
    fd.append('access_token', token)
    http.post(`/`, fd).then(data => {
      console.log(data.data)
      localStorage.setItem('username', data.data.user);
    });
  }

  logout() {
    localStorage.removeItem('username');
    localStorage.removeItem('spotify_token');
  }

}

export default new SpotifyDataService()
