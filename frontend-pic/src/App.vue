<template>
  <nav>
    <router-link to="/login">Login</router-link>
    <router-link to="/register">Register</router-link>
  </nav>
  <router-view/>
  <div class="OuterDiv">
    <FillDiv></FillDiv>

    <div class="InnerDiv">
      <FileUpload></FileUpload>
      <FeedDiv></FeedDiv>
    </div>
    <UserCreds :pic_url="pic_url"></UserCreds>
  </div>

</template>


<script>
import FileUpload from './components/FileUpload.vue'
import UserCreds from './components/UserCreds.vue'
import FillDiv from './components/FillDiv.vue'
import FeedDiv from './components/FeedDiv.vue'

export default {
  name: 'App',
  components: {
    FileUpload,
    UserCreds,
    FillDiv,
    FeedDiv
  },
  data(){
    return{ 
      loggedIn: false,
      username: null,
      id: null,
      pic_url: require("../test_data/logo.png"),

    }
  },
  methods: {
    onSignIn (user){
      console.log(user)
    }
  }
}

</script>
<style>
#app {
  margin: auto;
  width: 60%;
  background-color: black;
  height: 50em;
  display: flex;
  border-top: 5px solid black;
  border-left: 5px solid black;
  border-right: 5px solid black;

}
.OuterDiv{
  width: 100%;
  height: 100%;
  display: flex;
}
.InnerDiv{
  width: 50%;
  height: 100%;
}
</style>
