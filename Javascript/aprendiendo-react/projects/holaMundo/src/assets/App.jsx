import React from 'react'
import './App.css'
import { TwitterFollowCard } from './TwitterFolloCard'
export function App () {
    return(
        <section className='App'>
            <React.Fragment>
                <TwitterFollowCard userName="yamid-dev">
                    <h3>Yamid Horacio Rodríguez</h3>
                </TwitterFollowCard>

                <TwitterFollowCard 
                userName="midudev">
                    <h3>Miguel Ángel Durán García</h3>
                </TwitterFollowCard>

                <TwitterFollowCard
                userName="mouredev">
                    <h3>Brais Moure</h3>
                </TwitterFollowCard>

                <TwitterFollowCard      
                userName="MariaDev">
                    <h3>Maria Palomino</h3>
                </TwitterFollowCard>
            </React.Fragment>     
        </section>
    )
}