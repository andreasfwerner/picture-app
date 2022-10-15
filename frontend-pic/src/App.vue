<template>
  <nav >
    <router-link v-if="!loggedIn" to="/login">Login</router-link>
    <router-link v-if="!loggedIn" to="/register">Register</router-link>
  </nav>
  <router-view v-if="!loggedIn" @signedIn="signedIn"/>
  <TestDiv :user_id="1"/>


  <div v-if="loggedIn" class="OuterDiv">
    <FillDiv/>

    <div class="InnerDiv">
      <FileUpload :id="id"/>
      <FeedDiv/>
    </div>
    <UserCreds :pic_url="pic_url" :username="username" @signedOut="signOut"/>
  </div>


</template>


<script>
import FileUpload from './components/FileUpload.vue'
import UserCreds from './components/UserCreds.vue'
import FillDiv from './components/FillDiv.vue'
import FeedDiv from './components/FeedDiv.vue'


// TEST
import TestDiv from './components/TestPic.vue'


export default {
  name: 'App',
  components: {
    FileUpload,
    UserCreds,
    FillDiv,
    FeedDiv,
    TestDiv
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
