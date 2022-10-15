<template>
    <div class="UserDiv">
      <div class="EmptyFill"></div>
      <div class="HeartDiv">
        <div class="Filler">

        </div>
        <div class="SvgDiv">
          <a @click="fillHeart">
            <img class="Heart" ref="heart" :src="open_heart"/>
          </a>
        </div>
      </div>
    </div>
</template>
  
  <script>
  export default {
    name: 'FillDiv',
    data(){
      return{
        open_heart: require("../../svg/heart.svg"),
        closed_heart: require("../../svg/heartfill.svg")

      }
    }
    , 
    methods:{
      fillHeart(){
        if(this.$refs.heart.src.split("/img")[1] == this.open_heart.split("/img")[1]){
          this.$refs.heart.src = this.closed_heart
        }
        else{
          this.$refs.heart.src = this.open_heart
        }
        
      }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .UserDiv{
    width: 25%;
    height: 100%;
    background-color: black;
    display: flex;
    flex-direction: column;
  }
  .EmptyFill{
    height: 20%;
    width: 100%;
    background-color: black;
  }
  .HeartDiv{
    height: 80%;
    width: 100%;
    background-color: black;
  }
  .Filler{
    background-color:black;
    width: 100%;
    height: 25%;
  }
  .SvgDiv{
    width: 100%;
    height: 75%;
    background-color: black;
  }


  </style>
  