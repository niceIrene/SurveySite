function save(){
    var site = new Object;
    site.keyname = document.getElementById("keyname").value;
    site.sitename = document.getElementById("sitename").value;
    site.siteurl = document.getElementById("siteurl").value;
    var str = JSON.stringify(site); // 将对象转换为字符串
    localStorage.setItem(site.keyname,str);
    alert("保存成功");
}

function find(){
    var search_site = document.getElementById("search_site").value;
    var str = localStorage.getItem(search_site);
    var find_result = document.getElementById("find_result");
    var site = JSON.parse(str);
    find_result.innerHTML = search_site + "的网站名是：" + site.sitename + "，网址是：" + site.siteurl;
}