<template>
    <div class="ControlPanelDiv">
        <div class="UpDiv">
            <a @click="arrowUp">
                <img class="ArrowUp" src="../../svg/arrowdown.svg" />
            </a>
        </div>
        <div class="DownDiv">
            <a @click="arrowDown">
                <img class="ArrowDown" src="../../svg/arrowdown.svg" />
            </a>
        </div>
    </div>
</template>
  
  <script>
  export default {
    name: 'ControlPanel',
    props:{
        pic_len: Number
    },
    data(){
        return{
            curr:0
        }
    }
    ,
    methods:{
        arrowUp(){
            if (this.curr>0){
                this.curr--
                this.$emit('picUp',this.curr)
            }
        },
        arrowDown(){
            if (this.curr<this.pic_len-1){
                this.curr++
                this.$emit('picDown',this.curr)
            }
            
        }

    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .ControlPanelDiv{
    width: 50%;
    height: 80%;
    background-color: black;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
        .UpDiv{
            width: 100%;
            height: 30%;
            background-color: black;
        
        }
        a:hover{
            cursor:grab;
            
        }
        .DownDiv{
            width: 100%;
            height: 30%;
            background-color:black;
        }
                .ArrowDown{
                    transform: rotate(180deg);
                }
  </style>
  