<template>
    <div class="UserDiv">
      <div class="EmptyFill"></div>
      <div class="HeartDiv">
        <div class="Filler">

        </div>
        <div class="SvgDiv">
          <a>
            <img class="Heart" src="../../svg/heart.svg" />
          </a>
        </div>
      </div>
    </div>
</template>
  
  <script>
  export default {
    name: 'FillDiv',
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
  Heart{
    margin: auto;
  }
  </style>
  