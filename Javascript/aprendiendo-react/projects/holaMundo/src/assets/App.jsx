import React from 'react'
import './App.css'
import { TwitterFollowCard } from './TwitterFolloCard'
export function App () {
    return(
        <section className='App'>
            <React.Fragment>
                <TwitterFollowCard isFollowing userName="yamid-dev">
                    <strong>Yamid Horacio Rodríguez</strong>
                </TwitterFollowCard>

                <TwitterFollowCard 
                isFollowing={false} userName="midudev">
                    <strong>Miguel Ángel Durán García</strong>
                </TwitterFollowCard>      
            </React.Fragment>     
        </section>
    )
}