const userDropdownToggle = document.getElementById('userDropdownToggle');
const dropdownMenu = document.getElementById('dropdownMenu');

// 添加点击事件处理程序
userDropdownToggle.addEventListener('click', function (event) {
    // 切换下拉菜单的显示状态
    dropdownMenu.classList.toggle('show');
    // 阻止事件冒泡，以防止下拉菜单显示后立即隐藏
    event.stopPropagation();
});

// 在点击菜单以外的地方时隐藏下拉菜单
window.addEventListener('click', function (event) {
    if (!userDropdownToggle.contains(event.target) && dropdownMenu.classList.contains('show')) {
        dropdownMenu.classList.remove('show');
    }
});