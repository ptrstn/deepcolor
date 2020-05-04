import React from 'react';
import { render } from '@testing-library/react';
import App from './App';

test('test for Imaginator text in App', () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/Imaginator/i);
  expect(linkElement).toBeInTheDocument();
});
