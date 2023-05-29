var updateBtns = document.getElementsByClassName('update-like')

for (i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var truyenId = this.dataset.truyen
        var action = this.dataset.action
        console.log('truyenId',truyenId,'action',action)
        console.log('user',user)
        if (user === "AnonymousUser"){
            console.log('user not logged in')
        }
        else{
            updateUserLike(truyenId,action)
        }
    })
}

function updateUserLike(truyenId,action){
    console.log('user logged in')
    var url = '/like_truyen/'
    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body: JSON.stringify({'truyenId':truyenId,'action':action})
    })
    .then((response) => {
       return response.json()
    })
}