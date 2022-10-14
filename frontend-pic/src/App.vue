<template>
  <nav >
    <router-link v-if="!loggedIn" to="/login">Login</router-link>
    <router-link v-if="!loggedIn" to="/register">Register</router-link>
  </nav>

  <router-view v-if="!loggedIn" @signedIn="signedIn"/>


  <div v-if="loggedIn" class="OuterDiv">
    <FillDiv></FillDiv>

    <div class="InnerDiv">
      <FileUpload :id="id"></FileUpload>
      <FeedDiv></FeedDiv>
    </div>
    <UserCreds :pic_url="pic_url" :username="username" @signedOut="signOut"></UserCreds>
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
    signedIn (user){
      this.loggedIn = user.loggedIn;
      this.username = user.username;
      this.id = user.id;
    },
    signOut (state){
      this.loggedIn = state; 
      this.loggedIn = null;
      this.username = null;
      this.id = null;
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
