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
            userName="yamiddev" 
            name="Yamid Horacio Rodríguez"/>

            <TwitterFollowCard
            formattedUserName = {formattedUserName} 
            userName="midudev" 
            name="Mauricio Rozo" />

            <TwitterFollowCard
            formattedUserName = {formattedUserName}
            userName="christian" 
            name="Christian Martinez"/>

            <TwitterFollowCard
            formattedUserName = {formattedUserName} 
            userName="valexd" 
            name="Valentina Velandia"/>
        </section>
    )
}