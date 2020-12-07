import axios from "axios";

// var path = this.$router.resolve({name: 'Home'}).href

export default axios.create({
	baseURL: "http://35.224.48.117:5000/",
  headers: {
    "Content-type": "application/json",
  }
});
