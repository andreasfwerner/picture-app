<template>
  <nav >
    <router-link v-if="!loggedIn" to="/login">Login</router-link>
    <router-link v-if="!loggedIn" to="/register">Register</router-link>
  </nav>
  <router-view v-if="!loggedIn" @signedIn="signedIn"/>

  <div v-if="loggedIn" class="OuterDiv">
    <FillDiv/>

    <div class="InnerDiv">
      <FileUpload :id="id"/>
      <FeedDiv ref="feed" :user_id="id" @initPic="sendLength" :curr="curr"/>
    </div>
    <UserCreds :pic_url="pic_url" :username="username" :pic_len="pic_len" @picUp="picUp" @picDown="picDown" @signedOut="signOut"/>
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
      curr:0,
      pic_len:0

    }
  },
  methods: {
    signedIn (user){
      this.loggedIn = user.loggedIn;
      this.username = user.username;
      this.id = user.id;

      setTimeout(() => {    
        this.$refs.feed.getPicture();  
        },"500")
    },
    signOut (state){
      this.loggedIn = state; 
      this.loggedIn = null;
      this.username = null;
      this.id = null;
    },
    sendLength(l){
      this.pic_len = l;
    },
    picUp(curr){
      this.curr = curr;
      this.$refs.feed.updatePic()
    },
    picDown(curr){
      this.curr = curr;
      this.$refs.feed.updatePic()
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
