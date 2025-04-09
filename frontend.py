import React, { useState } from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';

export default function PhishNukeApp() {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleCheckUrl = async () => {
    setLoading(true);
    try {
      const res = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url })
      });

      const data = await res.json();
      setResult(data.prediction);
    } catch (error) {
      setResult('Error checking URL.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
      <Card className="max-w-xl w-full p-6 shadow-xl">
        <CardContent>
          <h1 className="text-2xl font-bold mb-4">PhishNuke: URL Phishing Detector</h1>
          <Input
            type="text"
            placeholder="Enter a URL to check..."
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            className="mb-4"
          />
          <Button onClick={handleCheckUrl} disabled={loading}>
            {loading ? 'Checking...' : 'Check URL'}
          </Button>
          {result && (
            <p className="mt-4 text-lg font-semibold">
              Result: <span className={result === 'Phishing' ? 'text-red-600' : 'text-green-600'}>{result}</span>
            </p>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
