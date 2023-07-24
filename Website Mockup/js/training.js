window.onload = function () {
    let images = ['img/SW4L.png', 'img/AC6.png'];

    let index = 0;
    const imgElement = document.getElementById("bottomPicture");
    
    function change() {
       imgElement.src = images[index];
       index >= 1 ? index = 0 : index++;
    }
    
    setInterval(change, 5000);
};