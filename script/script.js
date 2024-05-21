const btn = document.querySelector('#dark_button');
    
function dark_mode(){
    const body = document.querySelector('body')
    body.style.backgroundColor = 'HexCode'
}
btn.addEventListener('click',dark_mode)
