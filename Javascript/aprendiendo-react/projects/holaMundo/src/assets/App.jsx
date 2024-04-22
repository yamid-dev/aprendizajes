import React from 'react'
import './App.css'
import { TwitterFollowCard } from './TwitterFolloCard'
export function App () {
    //Esto es un elemento
    const formattedUserName = <span>@YamidDev</span>
    //esto es un componente reutilizable 
    return(
        <section className='App'>
            <TwitterFollowCard 
            formattedUserName = {formattedUserName}
            userName="yamid-dev" 
            name="Yamid Horacio Rodríguez"/>

            <TwitterFollowCard
            formattedUserName = {formattedUserName} 
            userName="midudev" 
            name="Miguel Ángel Durán García" />

            <TwitterFollowCard
            formattedUserName = {formattedUserName}
            userName="mouredev" 
            name="Brais Moure"/>

            <TwitterFollowCard
            formattedUserName = {formattedUserName} 
            userName="MariaDev" 
            name="Maria Dev"/>
        </section>
    )
}