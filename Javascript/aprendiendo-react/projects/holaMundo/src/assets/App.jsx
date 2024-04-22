import React from 'react'
import './App.css'
import { TwitterFollowCard } from './TwitterFolloCard'
export function App () {

    /*Children
        <TwitterFollowCard userName="yamid-dev">
            <h3>Yamid Horacio Rodríguez</h3> <--- children
        </TwitterFollowCard>
    */
    const yamiddev = {isFollowing : true, userName : 'yamid-dev'}
    const midudev = {isFollowing : true, userName : 'midudev'}
    const mouredev = {isFollowing : true, userName : 'mouredev'}
    const mariadev = {isFollowing : true, userName : 'soyDalto'}
    return(
        <section className='App'>
            <React.Fragment>
                <TwitterFollowCard {...yamiddev}>
                    <h3>Yamid Horacio Rodríguez</h3>
                </TwitterFollowCard>

                <TwitterFollowCard  {...midudev}>
                    <h3>Miguel Ángel Durán García</h3>
                </TwitterFollowCard>

                <TwitterFollowCard
                {...mouredev}>
                    <strong>Brais Moure</strong>
                </TwitterFollowCard>

                <TwitterFollowCard      
                {...mariadev}>
                    <strong>Maria Palomino</strong>
                </TwitterFollowCard>
                
            </React.Fragment>     
        </section>
    )
}