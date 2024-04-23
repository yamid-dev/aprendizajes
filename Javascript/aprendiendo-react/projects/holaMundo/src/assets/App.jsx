import React from 'react'
import './App.css'
import { TwitterFollowCard } from './TwitterFolloCard'
export function App () {
    // initialIsFollowing sólo se inicializa una vez
    return(
        <section className='App'>
            <React.Fragment>
                <TwitterFollowCard 
                initialIsFollowing = {true} 
                userName="yamid-dev">
                    <strong>Yamid Horacio Rodríguez</strong>
                </TwitterFollowCard>     
            </React.Fragment>     
        </section>
    )
}