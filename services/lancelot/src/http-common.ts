import axios from "axios";

// var path = this.$router.resolve({name: 'Home'}).href

export default axios.create({
  baseURL: "http://10.4.1.184:5000/",
  headers: {
    "Content-type": "application/json"
  }
});
