import { render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import App from './App'

describe('App', () => {
  it('renders the project placeholder', () => {
    render(<App />)

    expect(
      screen.getByRole('heading', {
        name: 'Warehouse & Smart Inventory Management',
      }),
    ).toBeInTheDocument()
  })
})
