from numpy import zeros
def pwLEval(a,b,x,zVals):
     '''
     % LVals = pwLEval(a,b,x,zvals)
     % Evaluates the piecewise linear polynomial defined by the column (n-1)-vectors
     % a and b and the column n-vector x. It is assumed that x(1) < ... < x(n).
     % zVals  is a column m-vector with each component in [x(1),x(n)].
     %
     % LVals is a column m-vector with the property that LVals(j) = L(zVals(j)) 
     % for j=1:m where L(z)= a(i) + b(i)(z-x(i)) for x(i)<=z<=x(i+1).
     '''

     m = len(zVals); 
     LVals = zeros(m,1); 
     g = 1;
     for j in range (1,m):
        i = Locate(x,zVals(j),g);
        LVals[j] = a(i) + b(i)*(zVals(j)-x(i));
        g = i;