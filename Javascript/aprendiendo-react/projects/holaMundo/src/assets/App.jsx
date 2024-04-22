import React from 'react'
import './App.css'
import { TwitterFollowCard } from './TwitterFolloCard'
export function App () {

    /*Children
        <TwitterFollowCard userName="yamid-dev">
            <h3>Yamid Horacio Rodríguez</h3> <--- children
        </TwitterFollowCard>
    */

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
                    <strong>Brais Moure</strong>
                </TwitterFollowCard>

                <TwitterFollowCard      
                userName="MariaDev">
                    <strong>Maria Palomino</strong>
                </TwitterFollowCard>
                
            </React.Fragment>     
        </section>
    )
}