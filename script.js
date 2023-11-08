function bossinfo(boss)
{
    value = isvisible(boss)
    console.log(value)
    if (value)
    {
        document.getElementById(boss).style.visibility = 'hidden';
    }
    else
    {
        document.getElementById(boss).style.visibility = 'visible';
    }
    console.log(isvisible(boss));

}
function isvisible(elem){
    let style = document.getElementById(elem)
    console.log(style.style.visibility)
    if (style.style.visibility == 'visible'){
        console.log('visible')
        return true;
    } 
    else{
        console.log('hidden')
        return false
    }
}