
class soluton{

    // Function to remove all spaces in a string
static int removeSpaces(char[] plain, int ps)
{
int i, count = 0;
for (i = 0; i < ps; i++)
if (plain[i] != '\u0000')
plain[count++] = plain[i];

return count;
}
}