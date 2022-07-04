const currentLang = document.location.href.includes('/es/') ? 'es' : 'en'
const changeLanguageTitle = currentLang==='es' ? 'Cambiar idioma' : 'Change language'
const langSelector = `

<div class="menu-dropdown menu-dropdown-repository-buttons">
  <button class="headerbtn menu-dropdown__trigger" aria-label="${changeLanguageTitle}">
      <i class="fas fa-globe"></i>
  </button>
  <div class="menu-dropdown__content">
    <ul>
      <li>
        <a class="headerbtn" data-toggle="tooltip" data-placement="left" title="" href='/en' onclick='return gotoLang("en")' >
            <span class="headerbtn__text-container">English</span>
        </a>
      </li>
      
      <li>
        <a class="headerbtn" data-toggle="tooltip" data-placement="left" title="" href='/es' onclick='return gotoLang("es")'>
            <span class="headerbtn__text-container">Español</span>
        </a>
      </li>
    </ul>
  </div>
</div>
`

function gotoLang(code) {
    try {
        const previuos = code === 'es' ? '/en/' : '/es/'
        const newCode = `/${code}/`
        if (document.location.href.includes(previuos)){
            document.location.href = document.location.href.replace(previuos,newCode)
        }
        return false
    } catch (error) {
        console.log(error)
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const parent = document.querySelector('.header-article__right')
    if (parent){
        parent.innerHTML = parent.innerHTML + langSelector
    }
})
