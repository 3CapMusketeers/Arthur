import axios from "axios";

// var path = this.$router.resolve({name: 'Home'}).href

export default axios.create({
  baseURL: "http://35.196.118.75/",
  headers: {
    "Content-type": "application/json"
  }
});
