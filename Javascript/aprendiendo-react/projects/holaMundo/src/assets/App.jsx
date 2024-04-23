import React from 'react'
import './App.css'
import { TwitterFollowCard } from './TwitterFolloCard'
export function App () {
    return(
        <section className='App'>
            <React.Fragment>
                <TwitterFollowCard userName="yamid-dev">
                    <strong>Yamid Horacio Rodríguez</strong>
                </TwitterFollowCard>

                <TwitterFollowCard 
                userName="midudev">
                    <strong>Miguel Ángel Durán García</strong>
                </TwitterFollowCard>

                <TwitterFollowCard
                userName="mouredev">
                    <strong>Brais Moure</strong>
                </TwitterFollowCard>

                <TwitterFollowCard      
                userName="SoyDalto">
                    <strong>Lucas Dalto </strong>
                </TwitterFollowCard>
                
            </React.Fragment>     
        </section>
    )
}