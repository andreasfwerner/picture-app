<template>
    <div class="Wrapper">
    <div class="UserDiv">
        <div class="UserProfilePic">
            <img :src="pic_url" alt="profile picture">
        </div>
        <div class="UserWrapper">
            <div class="UserName">
                <h3>{{ username }}</h3>
            </div>
            <div class="UserLogout">
                <button class="glow-on-hover" @click="this.$emit('signedOut',false)">Logout</button>
                <button class="glow-on-hover">Settings</button>
            </div>
        </div>
    </div>
    <div class="UserDivFill">
      <ControlPanel @picDown="picDown" @picUp="picUp" :pic_len="pic_len"></ControlPanel>
    </div>
    </div>
</template>
  
  <script>
  import ControlPanel from './ControlPanel.vue'
  export default {
    name: 'UserCreds',
    props:{
      pic_url:String,
      username:String,
      pic_len: Number
    },
    components: {
        ControlPanel
    },
    methods:{
      picDown(curr){
        this.$emit('picUp',curr)
      },
      picUp(curr){
        this.$emit('picDown',curr)
      }
    }
    
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .Wrapper{
    display: flex;
    height: 100%;
    width: 25%;
    flex-direction: column;
  }
  .UserDiv{
    width: 100%;
    height: 20%;
    background-color: black;
    display: flex;
  }
  .UserDivFill{
    width: 100%;
    height:80%;
    background-color: black;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .UserProfilePic{
    width: 7em;
    height: 7em;
    border-radius: 50%;
    background-color: wheat;
    background-position: 50% 50%;
  }
  .UserWrapper{
    width: 45%;
    height: 100%;
    background-color:black;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .UserName{
    width: 100%;
    height: 50%;
    background-color: black;
  }
  .UserName h3{
    color: white;
  }
  .UserLogout{
    width: 100%;
    height: 50%;
    background-color: black;
  }
  img{
    width: 7em;
    height: 7em;
    border-radius: 50%;
  }

  .glow-on-hover  {
    width: 70%;
    height: 30%;
    border: none;
    outline: none;
    color: #fff;
    background: #111;
    cursor: pointer;
    position: relative;
    z-index: 0;
    border-radius: 10px;
    margin:2%;
  }
  
  .glow-on-hover:before {
    content: '';
    background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
    position: absolute;
    top: -2px;
    left:-2px;
    background-size: 400%;
    z-index: -1;
    filter: blur(5px);
    width: calc(100% + 4px);
    height: calc(100% + 4px);
    animation: glowing 20s linear infinite;
    opacity: 0;
    transition: opacity .3s ease-in-out;
    border-radius: 10px;
  }
  
  .glow-on-hover:active {
    color: #000
  }
  
  .glow-on-hover:active:after {
    background: transparent;
  }
  
  .glow-on-hover:hover:before {
    opacity: 1;
  }
  
  .glow-on-hover:after{
    z-index: -1;
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: #111;
    left: 0;
    top: 0;
    border-radius: 10px;
  }
  
  
  @keyframes glowing {
    0% { background-position: 0 0; }
    50% { background-position: 400% 0; }
    100% { background-position: 0 0; }
  }
  
    h2{
      margin: auto;
      color: aliceblue;
    }
  
  </style>
  