export function TwitterFollowCard ({formattedUserName,userName,name}){
    return(
        <article className='tw-followCard'>
            <header className='tw-followCard-header'>
                <img className='tw-followCard-avatar' src="https://scontent.fbog4-1.fna.fbcdn.net/v/t39.30808-6/370379864_1036709290857076_2337778916240228598_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeFUV0OAeXCc3ozipSnYEsZF6knXuZE33fPqSde5kTfd84ESUCN3IXMKWnVhh-sTuP-4eswsqZwZJmkliPP1oJWE&_nc_ohc=15xnB80K4E8Ab6U-mF7&_nc_ht=scontent.fbog4-1.fna&oh=00_AfB3tb_7_nensuZo4cFu11ljDXPU122tKn4XqfiuAgCJYA&oe=662BDC4B" alt="imagen" />
                <div className='tw-followCard-info'>
                    <strong>{name}</strong>
                    <span className='tw-followCard-infoUserName'>{formattedUserName}</span>
                </div>
            </header>
            < aside>
                <button className='tw-followCard-button'>
                    Seguir
                </button>
            </aside>
        </article>
    )
}