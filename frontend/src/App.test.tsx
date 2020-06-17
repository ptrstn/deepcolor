import React from 'react';
import { render } from '@testing-library/react';
import App from './App';

test('test for Imaginator text in App', () => {
  const { queryAllByText } = render(<App />);
  const linkElement = queryAllByText(/Imaginator/i);
  expect(linkElement.length).toBeGreaterThan(0);
});
