public class Encap {
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String newName) {
        this.name = newName;
    }

    public static void main(String[] args) {
        Encap myobj = new Encap();
        myobj.setName("Harry");
        System.out.println(myobj.getName());
    }

}
