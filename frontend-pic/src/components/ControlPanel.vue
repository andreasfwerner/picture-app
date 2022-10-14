<template>
    <div class="ControlPanelDiv">
        <div class="UpDiv">
            <a>
                <img class="ArrowUp" src="../../svg/arrowdown.svg" />
            </a>
        </div>
        <div class="DownDiv">
            <a>
                <img class="ArrowDown" src="../../svg/arrowdown.svg" />
            </a>
        </div>
    </div>
</template>
  
  <script>
  export default {
    name: 'ControlPanel',
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
                .ArrowUp{

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
  