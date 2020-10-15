import axios from "axios";

// var path = this.$router.resolve({name: 'Home'}).href

export default axios.create({
  baseURL: process.env.ROOT_API,
  headers: {
    "Content-type": "application/json"
  }
});
